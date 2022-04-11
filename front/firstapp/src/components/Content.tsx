import React from 'react';
import {Route, Switch} from 'react-router-dom';
import '../App.css';
import {ContentComponentStyled} from '../styledComponent/ContentComponent-styled';
import Upload from "../contentComponents/Upload";
import Home from '../contentComponents/Home';

const ContentComponent: React.FC = () => (
    <ContentComponentStyled>
        <Switch>
            <Route path="/home">
                <Home/>
            </Route>

            <Route path="/">
                <Upload/>
            </Route>
        </Switch>
    </ContentComponentStyled>
)

export default ContentComponent;