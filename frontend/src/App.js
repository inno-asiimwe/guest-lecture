import Form from './components/Form'
import List from './components/List'
import './App.css';
import { useState } from 'react';

function App() {
  const [urls, setUrls] = useState([])
  const [visibility, setvisibility] = useState(false)
  return (
    <div className="App">
      <main className="App-header">
        <Form setUrls={setUrls} visibility={visibility} setvisibility={setvisibility}/>
        {urls.length > 0 && <List urls={urls} visibility={visibility}/>}
      </main>
    </div>
  );
}

export default App;
