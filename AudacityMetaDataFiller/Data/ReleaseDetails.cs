using DiscogsClient.Data.Result;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AutomaticTrackDetails.Data
{
    public class ReleaseDetails
    {
        public string Title { get; set; } 
        public string ArtistName { get; set; } 
        public string Release { get; set; }
        public List<string> Genres { get; set; }
        public int Year { get; set; }
        public List<DiscogsTrack> Tracklist { get; set; }
        public int? TrackNumber { get; set; }
        public List<string> Styles { get; set; }
    }
}
