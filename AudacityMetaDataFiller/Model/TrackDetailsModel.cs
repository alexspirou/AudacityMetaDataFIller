using AutomaticTrackDetails.Data;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AutomaticTrackDetails.Model
{
    public class TrackDetailsModel
    {
        private readonly ITrackDetailsProvider _trackDetailsProvider;
        public TrackDetailsModel(ITrackDetailsProvider discogsClient)
        {
            _trackDetailsProvider = discogsClient;
        }

        public async Task<ReleaseDetails> GetReleaseDetailsAsync(int id)
        {
            return await _trackDetailsProvider.GetReleasyByIdAsync(id);
        }
    }
}
