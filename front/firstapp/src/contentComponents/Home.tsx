import React from 'react';
import '../App.css';
import {HomeStyled} from "./Home-styled";
import {TextStyled} from "../styledComponent/TextStyled";
import {TextFilledStyled} from "../styledComponent/TextFilled-styled";
import {ButtonFilledStyled} from '../styledComponent/ButtonFilled-styled';
import {ButtonStyled} from '../styledComponent/Button-styled';
import {useHistory} from "react-router-dom";
import ReactPlayer from 'react-player';

const Home: React.FC = () => {

    const history = useHistory();
    const exitToHome = () => {
        history.push('/')
    };
    return (
        <HomeStyled>

            <ReactPlayer url="ссыль тут" />

            <ButtonFilledStyled width={100} height={20} justifycontent={'space-between'}>
                <ButtonStyled onClick={exitToHome}>
                    Exit
                </ButtonStyled>
            </ButtonFilledStyled>

        </HomeStyled>

    )
}


export default Home;