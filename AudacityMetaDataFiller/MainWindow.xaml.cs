using AutomaticTrackDetails.Model;
using AutomaticTrackDetails.VieModels;
using LandisGyr.E450.PlcOpticalUpgradeHelperTool.Data;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace AutomaticTrackDetails
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        TrackDetailsViewModel _trackDetailsViewModel;
        public MainWindow()
        {
            _trackDetailsViewModel = new TrackDetailsViewModel(new TrackDetailsModel(new DiscogsClientService() ), new LocalSocket());
            DataContext = _trackDetailsViewModel;
            InitializeComponent();
        }
    }
}
