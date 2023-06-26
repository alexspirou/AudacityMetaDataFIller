using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AutomaticTrackDetails.Services
{
    public interface ILocalSocket
    {
        void Connect();
        void Disconnect();
        void Abort();
        void Reconnect();
        string ReceiveData();
        void SendData(string msg);
        bool IsConnected { get;  }
    }
}
