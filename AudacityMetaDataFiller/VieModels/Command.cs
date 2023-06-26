using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Input;

namespace AutomaticTrackDetails.VieModels
{
    public class Command : ICommand
    {
        public Action Action { get; set; }

        public Command(Action action)
        {
            Action = action;
        }

        public event EventHandler? CanExecuteChanged = delegate { };

        public void Execute(object param)
        {
            Action?.Invoke();
        }

        public bool CanExecute(object? parameter)
        {
            return true;
        }
    }
}
