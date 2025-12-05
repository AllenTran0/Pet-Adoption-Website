import { useAuth0 } from "@auth0/auth0-react";

const Profile = () => {
  const { user, isAuthenticated } = useAuth0();

  return (
    isAuthenticated && (
      <div>
        <h2>{user.name}</h2>
        <p>{user.username}</p>
        <p>{user.birthdate}</p>
        <p>{user.bio}</p>
      </div>
    )
  );
};

export default Profile;