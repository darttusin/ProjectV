import styled from "styled-components";
import {Button} from "antd";
import {ButtonProps} from "antd/es";
import {SizeType} from "antd/lib/config-provider/SizeContext";

export interface ButtonStyledProps extends ButtonProps {
    fontSize?: number
    size?: SizeType;

}

export const ButtonStyled = styled(Button)`
  font-size: ${(p: ButtonStyledProps) => p?.fontSize}15px;
  //size: ${(p: ButtonStyledProps) => p?.size}large;
  border-radius: 8px;
  border: 1px solid deepskyblue;
`
