import { useAuth0 } from "@auth0/auth0-react";
import { LoginButton } from "./loginbutton";
import { SignupButton } from "./signup";
import { LogoutButton } from "./logout";

export const NavBarButtons = () => {
  const { isAuthenticated } = useAuth0();

  return (
    <div className="nav-bar__buttons">
      {!isAuthenticated && (
        <>
          <SignupButton />
          <LoginButton />
        </>
      )}
      {isAuthenticated && (
        <>
          <LogoutButton />
        </>
      )}
    </div>
  );
};