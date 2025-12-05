import { BrowserRouter, Route, Routes } from "react-router-dom";
import Home from "./pages/Home";
import About from "./pages/About";
import { Settings } from "./pages/Settings";
import Navbar_pet from "./components/Navbar";
import DogPage from "./pages/DogPage";
import CatPage from "./pages/CatPage";
import { SettingsProvider } from "./components/Settingsimport";
import { Questionnaire } from "./pages/Questionare";
import Shop from "./pages/Shop";
import ToysPage from "./pages/Toys";
import FoodPage from "./pages/Food";
import BedsPage from "./pages/Beds";
import Accessories from "./pages/Accessories";

import { Auth0ProviderWithNavigate } from "./components/auth0-provider-wrapper";


const App = () => {

  // const { isLoading, error } = useAuth0();

  // if (error) {
  //   return <div>Oops... {error.message}</div>;
  // }

  // if (isLoading) {
  //   return <Loading />;
  // }

  return (

    <BrowserRouter>
    <Auth0ProviderWithNavigate>
    <SettingsProvider>
    <Navbar_pet></Navbar_pet>
      <Routes>
        <Route path="/settings" element={<Settings />} />
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/dog" element={<DogPage />} />
        <Route path="/cat" element={<CatPage />} />
        <Route path="/pet_quiz" element={<Questionnaire></Questionnaire>} />
        <Route path="/shop" element={<Shop />} />
        <Route path="/shop/Toys" element={<ToysPage />} />
        <Route path="/shop/Food" element={<FoodPage />} />
        <Route path="/shop/Beds" element={<BedsPage />} />
        <Route path="/shop/Accessories" element={<Accessories />} />
      </Routes>
      </SettingsProvider>
      </Auth0ProviderWithNavigate>
    </BrowserRouter>
  )
}

export default App;