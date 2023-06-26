using AutomaticTrackDetails.Services;
using System;
using System.Net;
using System.Net.Sockets;
using System.Text;

namespace LandisGyr.E450.PlcOpticalUpgradeHelperTool.Data
{
    public class LocalSocket : ILocalSocket
    {
        private string _connectionIP = "127.0.0.1";
        private int _connectionPort = 25001;
        private IPAddress _localAdd;
        private TcpListener _listener;
        private TcpClient _client;
        private NetworkStream _nwStream;

       public bool IsConnected { get; private set; }
        public void Connect()
        {
            _localAdd = IPAddress.Parse(_connectionIP);
            _listener = new TcpListener(IPAddress.Any, _connectionPort);
            _listener.Start();
            _client = _listener.AcceptTcpClient();
            _nwStream = _client.GetStream();
            IsConnected = _client.Connected;
        }

        public void Disconnect()
        {
            _listener?.Stop();
            _listener.Server.Close();
        }
    
        public void Abort()
        {
            this.Abort();
        }
        public void Dispose()
        {
            this.Dispose();
        }

        public void Reconnect()
        {
            Console.WriteLine("Trying to connect...");
            _listener.Stop();
            _localAdd = IPAddress.Parse(_connectionIP);
            _listener = new TcpListener(IPAddress.Any, _connectionPort);
            _listener.Start();

            _client = _listener.AcceptTcpClient();

        }

        public string ReceiveData()
        {
            byte[] buffer = new byte[_client.ReceiveBufferSize];

            int bytesRead = _nwStream.Read(buffer, 0, _client.ReceiveBufferSize); //Getting data in Bytes from Python
            string dataReceived = Encoding.UTF8.GetString(buffer, 0, bytesRead); //Converting byte data to string

            return dataReceived;
        }

        public void SendData(string msg)
        {
            byte[] myWriteBuffer = Encoding.ASCII.GetBytes(msg);
            _nwStream?.Write(myWriteBuffer, 0, myWriteBuffer.Length);
        }

    }
}