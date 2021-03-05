import React from 'react';
import { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [date, setDate] = useState(null);
  useEffect(() => {
    async function getDate() {
      const res = await fetch('/api/hello');
      const newDate = await res.text();
      setDate(newDate);
    }
    getDate();
  }, []);
  return (
    <main>
      <h1>Kamyar Ghasemlou</h1>
      <h2>
        Hi there, welcome to my homepage!
      </h2>
      <p>
        Intro.
      </p>
      <br />
      <h2>Backend says:</h2>
      <p>{date ? date : 'Loading date...'}</p>
    </main>
  );
}

export default App;
