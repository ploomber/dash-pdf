/* eslint no-magic-numbers: 0 */
import React, { useState } from 'react';

import { DashPdf } from '../lib';

const App = () => {

    const [state, setState] = useState({value:'', label:'Type Here'});
    const setProps = (newProps) => {
            setState(newProps);
        };

    return (
        <div>
            <DashPdf
                setProps={setProps}
                {...state}
            />
        </div>
    )
};


export default App;
