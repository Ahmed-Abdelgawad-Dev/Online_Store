import Footer from "./components/Footer";
import Header from "./components/Header";
import HomePage from "./pages/HomePage";
import { Routes, Route } from "react-router-dom";
import Test from "./components/Test";
function App() {
  return (
    <div className="App">
      <main>
        <Header />
        <Routes>
          <Route exact path="/" element={<HomePage />} />
          <Route exact path="/test" element={<Test />} />
        </Routes>
        <Footer />
      </main>
    </div>
  );
}

export default App;
