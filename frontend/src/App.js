
import React, { useEffect, useState } from 'react';

function App() {
  const [incidents, setIncidents] = useState({});

  useEffect(() => {
    fetch("http://localhost:8000/incidents")
      .then(res => res.json())
      .then(data => setIncidents(data));
  }, []);

  return (
    <div>
      <h1>IMS Dashboard</h1>
      {Object.keys(incidents).map(key => (
        <div key={key}>
          <h3>{key}</h3>
          <p>Status: {incidents[key].status}</p>
        </div>
      ))}
    </div>
  );
}

export default App;
