import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import SchoolInfoManagement from "./pages/SchoolInfomationForm"; // Import your SchoolInfoManagement component
import SchoolBranding from './components/SchoolBranding'; // Import your SchoolBranding component

function App() {
  return (
    <Router>
      <div>
        {/* Your navigation or header component can go here */}
        <Switch>
          <Route exact path="/school-info-management" component={SchoolInfoManagement} />
          <Route exact path="/school-branding" component={SchoolBranding} />
          {/* Add more routes for other submodules and tasks */}
        </Switch>
      </div>
    </Router>
  );
}

export default App;
