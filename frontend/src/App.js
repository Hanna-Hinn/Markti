import './App.css';
import main from './main';
import './main.css';
import footer from './footer';
import './footer.css'
function App() {
  return <nav>
  {main()}
  {footer()}
  </nav>;
    
}

export default App;
