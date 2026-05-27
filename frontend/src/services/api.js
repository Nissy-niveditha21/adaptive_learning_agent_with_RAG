const API_BASE = '/api';


// =========================
// START SESSION
// =========================
export const startSession = async () => {

  try {

    const response = await fetch(`${API_BASE}/start-session`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
    });

    if (!response.ok) {
      throw new Error('Failed to start session');
    }

    return await response.json();

  } catch (error) {

    console.error("Start Session API Error:", error);
    throw error;
  }
};


// =========================
// EVALUATE ANSWERS
// =========================
export const evaluateAnswers = async (answers) => {

  try {

    const response = await fetch(`${API_BASE}/evaluate`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        answers,
      }),
    });

    if (!response.ok) {
      throw new Error('Failed to evaluate answers');
    }

    return await response.json();

  } catch (error) {

    console.error("Evaluation API Error:", error);
    throw error;
  }
};


// =========================
// FUTURE APIs
// =========================
export const sendMessage = async (data) => {

  // Future chatbot endpoint

};