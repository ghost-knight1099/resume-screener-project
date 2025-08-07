import React, { useState } from 'react';
import './App.css';

function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [response, setResponse] = useState(null);

  const handleFileChange = (e) => {
    setSelectedFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!selectedFile) {
      alert("Please select a file first.");
      return;
    }

    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
      const res = await fetch("http://127.0.0.1:5000/upload", {
        method: "POST",
        body: formData
      });

      const data = await res.json();
      setResponse(data);
    } catch (err) {
      console.error("Error uploading file:", err);
      setResponse({ error: "Upload failed" });
    }
  };

  return (
    <div className="App">
      <h1>Resume Uploader</h1>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>
      {response && (
        <pre className="output">{JSON.stringify(response, null, 2)}</pre>
      )}
    </div>
  );
}

export default App;