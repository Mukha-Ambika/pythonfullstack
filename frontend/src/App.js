import "./App.css";
import React, { useState } from "react";

const App = () => {
  const [email, setemail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email_address: email, password: password }),
    };

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/login/",
        requestOptions
      );
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const data = await response.json();
      console.log("Login successful:", data);
      // Handle successful login (e.g., save token, redirect)
    } catch (error) {
      console.error("Login failed:", error);
      //  setError("Invalid credentials. Please try again.");
    }
  };

  return (
    <div className="login-container">
      <h2>Login</h2>
      <form onSubmit={handleLogin}>
        <div>
          <label htmlFor="email">email adddress:</label>
          <input
            type="text"
            id="email"
            value={email}
            onChange={(e) => setemail(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="password">Password:</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <button type="submit">Login</button>
      </form>
    </div>
  );
};

export default App;
