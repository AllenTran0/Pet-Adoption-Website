import { createRoot } from 'react-dom/client';
import { Auth0Provider } from '@auth0/auth0-react';
import App from './App';

const rootElement = document.getElementById('root') as HTMLElement;
const root = createRoot(rootElement);

root.render(
<Auth0Provider
    domain="dev-4n85xpqblsu5bgo1.us.auth0.com"
    clientId="ces5WPQNZyY3PO6Gnj8J2B1n0YyHY6Ee"
    authorizationParams={{
      redirect_uri: window.location.origin
    }}
  >
    <App />
  </Auth0Provider>,
);