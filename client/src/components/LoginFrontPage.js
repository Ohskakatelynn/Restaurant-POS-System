import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import FrontPage from './FrontPage';

function LoginFrontPage() {
  const history = useHistory();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loggedIn, setLoggedIn] = useState(false);

  const handleLogin = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch('http://127.0.0.1:5555/users');
      const users = await response.json();

      const foundUser = users.find(
        (user) => user.username === username && user.password === password
      );
      if (foundUser) {
        setError('');
        setLoggedIn(true);
        history.push('/FrontPage');
      } else {
        setError('Invalid login');
      }
    } catch (error) {
      console.error('Error occurred during login:', error);
      setError('Unable to process login');
    }
  };

  if (loggedIn) {
    return <FrontPage />;
  }

  return (
    <div>
      <h2>Login Page</h2>
      {error && <p>{error}</p>}
      <form onSubmit={handleLogin}>
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button type="submit">Login</button>
      </form>
    </div>
  );
}

export default LoginFrontPage;