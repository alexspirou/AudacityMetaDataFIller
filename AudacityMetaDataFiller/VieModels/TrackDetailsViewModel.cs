using AutomaticTrackDetails.Data;
using AutomaticTrackDetails.Model;
using AutomaticTrackDetails.Services;
using DiscogsClient.Data.Result;
using LandisGyr.E450.PlcOpticalUpgradeHelperTool.Data;
using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Diagnostics;
using System.Linq;
using System.Text.RegularExpressions;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Input;
using static System.Net.Mime.MediaTypeNames;

namespace AutomaticTrackDetails.VieModels;

public class TrackDetailsViewModel : ViewModelBase
{
    private readonly TrackDetailsModel _trackDetailsModel;
    private readonly ILocalSocket _localSocket;
    private ReleaseDetails _releaseDetails;
    private List<DiscogsTrack> _trackList;
    private CancellationTokenSource cts = new CancellationTokenSource();

    public TrackDetailsViewModel(TrackDetailsModel trackDetailsModel, ILocalSocket localSocket)
    {
        _trackDetailsModel = trackDetailsModel;
        _localSocket = localSocket;
        SaveValuesCommand = new Command(SaveValuesCommandClick);
        GetDetailsCommand = new Command(GetDetailsCommandClick);
        CancelPythonScriptCommand = new Command(CancelPythonScriptCommandClick);
    }


    #region Bindings

    public string? ArtistName { get; set; }
    public string? TrackTitle { get; set; }
    public string? AlbumTitle { get; set; }
    public string? TrackNumber { get; set; }
    public int? Year { get; set; }
    public string? Genre { get; set; }
    public string? Styles { get; set; }

    public string? Comments { get; set; }
    public int Id { get; set; } = 3744821;
    public ObservableCollection<string> Tracks { get; set; }

    public int _selectedIndex { get; set; } 
    public int SelectedIndex
    {
        get
        {
            return _selectedIndex;
        }
        set
        {
            _selectedIndex = value;
            OnPropertyChanged(nameof(SelectedIndex));
            IdentifyTrackPosition(SelectedIndex);
        }
    }

    public string _selectedTrack { get; set; }
    public string SelectedTrack
    {
        get
        {
            return _selectedTrack;
        }
        set
        {
            _selectedTrack = value;
            OnPropertyChanged(nameof(SelectedTrack));
            IdentifyTrackPosition(SelectedIndex);
        }
    }

    #endregion

    private void IdentifyTrackPosition(int position)
    {
        TrackNumber = _trackList[position].position;
    }

    #region Commands And Actions

    public ICommand CancelPythonScriptCommand { get; }
    private void CancelPythonScriptCommandClick()
    {
        cts.Cancel();
        string KillPythonProcessCommand = "/C wmic process where \"commandline like \'%%Debug.py%%\'\" delete";
        ExecuteProcess("CMD.exe", KillPythonProcessCommand);
    }

    public string ExecuteProcess(string filename, string arguments)
    {
        try
        {
            ProcessStartInfo startInfo = new ProcessStartInfo
            {
                Verb = "runas",
                FileName = filename,
                Arguments = arguments,
                WorkingDirectory = Environment.CurrentDirectory,
                WindowStyle = ProcessWindowStyle.Hidden,
                CreateNoWindow = true,
                UseShellExecute = false,
                RedirectStandardInput = true,
                RedirectStandardOutput = true,
                RedirectStandardError = true
            };
            Process process = new Process();
            process.StartInfo = startInfo;
            process.Start();
            process.WaitForExit();
            return process.StandardOutput.ReadToEnd();
        }
        catch (Exception ex)
        {
            throw new Exception("Exception caused while executing process '" + filename + " " + arguments + "' ", ex);
        }
    }
    public ICommand SaveValuesCommand { get; set; }
    private void SaveValuesCommandClick()
    {        
        string strCmdText;

        string ArtistNameTrimmed = ArtistName.Replace("&", "and").Replace(" ", "-");
        string SelectedTrackTrimmed = SelectedTrack.Replace("&", "and").Replace(" ", "-");
        string AlbumTitleTrimmed = AlbumTitle.Replace("&", "and").Replace(" ", "-");
        string GenreTrimmed = Genre.Replace("&", "and").Replace(" ", "-");
        string CommentsTrimmed = Comments.Replace("&", "and").Replace(" ", "-");

        string args = string.Format(@" {0} {1} {2} {3} {4} {5} {6}", ArtistNameTrimmed, SelectedTrackTrimmed, AlbumTitleTrimmed, TrackNumber, Year.ToString(), GenreTrimmed, CommentsTrimmed);
        //string args = string.Format(@" {0} {1} {2} {3} {4} {5} {6}", "ena", "duo", "tria", "tessera", "pente", "eksi", "efta");
        strCmdText = $@"/C cd C:\Users\alexs\source\repos\PythonAutoClick\PythonAutoClick && python Debug.py";

        System.Diagnostics.Process.Start("CMD.exe", strCmdText + args);
        var cancellationToken = cts.Token;

        var pythonSrcTask = Task.Factory.StartNew(() =>
        {
            if (!_localSocket.IsConnected)
            {
                _localSocket.Connect();
            }
            Thread.Sleep(3000);
            while(_localSocket.IsConnected)
            {
                var recievedData = _localSocket.ReceiveData();
                if(recievedData.Equals("Hello5"))
                {
                    break;
                }
            }
        }, cancellationToken);

        var waitToDisconnectTask = Task.Factory.StartNew(() =>
        {
            while(!pythonSrcTask.IsCompleted)
            {
                // Do nothing
            }
            cts.Cancel();
        });

    }

    public ICommand GetDetailsCommand { get; set; }
    private void GetDetailsCommandClick()
    {
        Task.Factory.StartNew( async () =>
        {
            _releaseDetails = await _trackDetailsModel.GetReleaseDetailsAsync(Id);
            ArtistName = _releaseDetails.ArtistName;
            AlbumTitle = _releaseDetails.Title;
            Year = _releaseDetails.Year;
            _trackList = _releaseDetails.Tracklist;
            var s = _trackList.Select(x => $"{x.title}").ToList();

            Genre = string.Join(",", _releaseDetails.Genres);
            Styles = string.Join(",", _releaseDetails.Styles);
            Tracks = new ObservableCollection<string>(s);
        });


       

    }
    #endregion
}
