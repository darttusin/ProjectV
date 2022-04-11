import styled from "styled-components";


type contentProps = 'center' | 'left' | 'right' | 'space-between'

interface InputFilledStyledProps {
    width: number
    height: number
    justifycontent: contentProps
}

export const InputFilledStyled = styled.div`
  width: ${(p: InputFilledStyledProps) => p.width}%;
  display: flex;
  flex-direction: inherit;
  border-radius: inherit;
  justify-content: ${(p: InputFilledStyledProps) => p.justifycontent};
  height: ${(p: InputFilledStyledProps) => p.height}px;
`