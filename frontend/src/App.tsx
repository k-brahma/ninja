import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Login from './components/Login';
import PostList from './components/PostList';
import MyPosts from './components/MyPosts';

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/login" component={Login} />
        <Route path="/posts" component={PostList} />
        <Route path="/myposts" component={MyPosts} />
      </Switch>
    </Router>
  );
}

export default App; 