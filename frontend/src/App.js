import React from 'react';
import Login from './components/Login';
import Welcome from './components/Welcome';

class App extends React.Component {
  state = {
    isLoggedIn: false
  };

  handleLogin = () => {
    this.setState({ isLoggedIn: true });
  };

  render() {
    return this.state.isLoggedIn ? <Welcome /> : <Login handleLogin={this.handleLogin} />;
  }
}

export default App;