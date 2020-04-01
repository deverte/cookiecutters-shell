"""{{cookiecutter.app_name}} controller."""

import dash

from dash.dependencies import Output, Input, State
from dash.exceptions import PreventUpdate

from {{cookiecutter.app_name}}.dash_app.app import app as dash_app

@dash_app.app.callback(
    Output('extra_block_div', 'hidden'),
    [Input('extra_block_store', 'modified_timestamp')],
    [State('extra_block_store', 'data')]
)
def extra_block_div_hidden_callback(ebs_mt: int, ebs_data: bool):
    """`extra_block_div` reacts on the `extra_block_store` changes.

    Changes visibility of the `extra_block_div` if `extra_block_store` is changed.
    Reacts on the `ebs_data_callback` callback.

    Args:
        ebs_mt: `extra_block_store`'s `modified_timestamp` (changes when it's data changes)
            property.
        ebs_data: `extra_block_store`'s `data` property.

    Returns:
        If `extra_block_store` is `True` then `extra_block_div`'s `hidden` property is `True`.
        And vice versa.

    Raises:
        PreventUpdate: If `extra_block_store`'s data isn't initialized.
    """
    if ebs_mt is None:
        raise PreventUpdate
    return ebs_data

@dash_app.app.callback(
    Output('extra_block_store', 'data'),
    [Input('show_hide_button', 'n_clicks')],
    [State('extra_block_store', 'data'),
     State('extra_block_store', 'modified_timestamp')]
)
def ebs_data_callback(shb_n_clicks: int, ebs_data: bool, ebs_mt: int):
    """`extra_block_store` reacts on the `show_hide_button` clicks.

    Every click changes `extra_block_store`'s `data` property on the opposite value.
    Causes `extra_block_div_hidden_callback` callback.

    Args:
        shb_n_clicks: `show_hide_button`'s `n_clicks` property.
        ebs_data: `extra_block_store`'s `data` property.
        ebs_mt: `extra_block_store`'s `modified_timestamp` (changes when it's data changes)
            property.

    Returns:
        On the startup, returns `is_hiden` initial data of the `extra_block_div`.
        In other cases changes `extra_block_div`'s value on the opposite.
    """
    if ebs_mt is None:
        return dash_app.initial_data.extra_block_div.is_hidden
    return not ebs_data