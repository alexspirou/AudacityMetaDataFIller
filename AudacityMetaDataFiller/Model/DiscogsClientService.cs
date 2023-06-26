using AutomaticTrackDetails.Data;
using DiscogsClient;
using DiscogsClient.Data.Query;
using DiscogsClient.Internal;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AutomaticTrackDetails.Model
{
    public class DiscogsClientService : ITrackDetailsProvider
    {
        DiscogsClient.DiscogsClient _discogsClient;
        public DiscogsClientService()
        {
            var tokenInformation = new TokenAuthenticationInformation("FhbMClnDjEAjjKptlnOJbxzLOeGXgzDJkxTDbrZD");
            _discogsClient = new DiscogsClient.DiscogsClient(tokenInformation);

        }

        public async Task<ReleaseDetails> GetReleasyByIdAsync(int id)
        {


            var release = await _discogsClient.GetReleaseAsync(id);

            var releaseDetails = new ReleaseDetails()
            {
                Title = release.title,
                ArtistName = release.artists_sort,
                Genres = release.genres.ToList(),
                Year = release.year,
                Tracklist = release.tracklist.ToList(),
                Styles = release.styles.ToList(),
              
            };

            return releaseDetails;

        }
    }
}
