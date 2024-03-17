import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    // Call your backend API here
  };

  return (
    <form onSubmit={handleSubmit} className="container mt-5">
      <div className="form-group">
        <label htmlFor="username">Username</label>
        <input type="text" className="form-control" id="username" value={username} onChange={e => setUsername(e.target.value)} placeholder="Username" />
      </div>
      <div className="form-group">
        <label htmlFor="password">Password</label>
        <input type="password" className="form-control" id="password" value={password} onChange={e => setPassword(e.target.value)} placeholder="Password" />
      </div>
      <button type="submit" className="btn btn-primary">Login</button>
    </form>
  );
}

export default Login;