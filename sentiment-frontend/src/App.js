import React, { useState } from "react";
import "./App.css";

function App() {
  const [text, setText] = useState("");
  const [result, setResult] = useState("");

  const handleSubmit = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ text })
      });

      const data = await response.json();
      setResult(data.sentiment);
    } catch (error) {
      console.error(error);
      setResult("Error: Could not connect to API");
    }
  };

  return (
    <div className="App">
      <h1>Twitter Sentiment Analysis</h1>
      <textarea
        placeholder="Enter a tweet..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <br />
      <button onClick={handleSubmit}>Analyze</button>
      <h2>Sentiment: {result}</h2>
    </div>
  );
}

export default App;
