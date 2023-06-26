using AutomaticTrackDetails.Data;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AutomaticTrackDetails.Model
{
    public interface ITrackDetailsProvider
    {
        Task<ReleaseDetails> GetReleasyByIdAsync(int id);
    }
}
