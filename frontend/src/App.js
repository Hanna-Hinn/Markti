import './App.css';
import main from './main';
import './main.css';
import footer from './components/footer';
import './components/footer.css'
function App() {
  return <div>
  {main()}
  {footer()}
  <main/>
  </div>;
    
}

export default App;
