import { useState } from "react";

export default function App() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);

  const startSession = async () => {
    setLoading(true);

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/start-session",
        {
          method: "POST",
        }
      );

      const result = await response.json();

      console.log(result);

      setData(result);
    } catch (error) {
      console.error("API Error:", error);
    }

    setLoading(false);
  };

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h1>AI Learning Agent</h1>

      <button onClick={startSession}>
        Start Learning Session
      </button>

      {loading && <p>Loading...</p>}

      {data && (
        <div style={{ marginTop: "30px" }}>
          <h2>Checkpoint</h2>

          <p>
            <strong>Topic:</strong> {data.topic}
          </p>

          <p>
            <strong>Current Checkpoint:</strong>{" "}
            {data.current_checkpoint.title}
          </p>

          <h3>Generated Questions</h3>

          <ul>
            {data.generated_questions.map((q, index) => (
              <li key={index}>{q}</li>
            ))}
          </ul>

          <h3>Feynman Explanation</h3>

          <p>{data.feynman_explanation}</p>

          <h3>Score</h3>

          <p>{data.score}</p>
        </div>
      )}
    </div>
  );
}