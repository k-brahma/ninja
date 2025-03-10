import React from 'react';
import { BrowserRouter as Router, Route, Switch, Redirect } from 'react-router-dom';
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
        {/* Add a default redirect to one of your routes */}
        <Route exact path="/">
          <Redirect to="/posts" />
        </Route>
      </Switch>
    </Router>
  );
}

export default App;