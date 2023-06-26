using AutomaticTrackDetails.VieModels;
using System.Windows;

namespace AutomaticTrackDetails
{
    /// <summary>
    /// Interaction logic for App.xaml
    /// </summary>
    public partial class App : Application
    {

        protected override void OnStartup(StartupEventArgs e)
        {

            var MainWindow = new MainWindow();

            base.OnStartup(e);
        }
    }
}
