import './App.css';

import HeaderComponent from "./components/Header";
import ContentComponent from "./components/Content";
import FooterComponent from "./components/Footer";
import {Layout} from "antd";


function App() {
    return (
        <Layout>
            <HeaderComponent/>
            <ContentComponent/>
            <FooterComponent/>
        </Layout>

    );
}

export default App;
