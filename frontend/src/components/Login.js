import React, { useState } from 'react';
import { useNavigation } from '@react-navigation/native';

import 'bootstrap/dist/css/bootstrap.min.css';


function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [showAlert, setShowAlert] = useState(false);
  const navigation = useNavigation();

  
  const handleSubmit = async (e) => {
    const response = await fetch(`${process.env.API_URL}:${process.env.API_PORT}/login`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        username,
        password
      })
    });
    const data = await response.json();

    if (response.ok) navigation.navigate('Welcome');
    else {
      console.log('Login failed:', data.message);
      setShowAlert(true);
    }

    e.preventDefault();
  };

  return (
    <>
      {showAlert && <Alert variant="danger">Usuario ou senha incorretos</Alert>}
      {
        <form onSubmit={handleSubmit} className="container mt-5">
          <div className="form-group mb-3">
            <label htmlFor="username">Username</label>
            <input type="text" className="form-control" id="username" value={username} onChange={e => setUsername(e.target.value)} placeholder="Username" />
          </div>
          <div className="form-group mb-3">
            <label htmlFor="password">Password</label>
            <input type="password" className="form-control" id="password" value={password} onChange={e => setPassword(e.target.value)} placeholder="Password" />
          </div>
          <button type="submit" className="btn btn-primary">Login</button>
        </form>
      }
    </>
  );
}

export default Login;