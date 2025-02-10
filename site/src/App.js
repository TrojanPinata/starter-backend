import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Page from "./Page";
import Home from "./Home";

export default function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="Page" element={<Page />} />
            </Routes>
        </BrowserRouter>
    );
}
  
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
