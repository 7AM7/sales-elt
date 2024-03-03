import pandas as pd
import plotly.express as px


@render(render_type="html")  # type: ignore # noqa
def r(df, *args, **kwargs):
    df = pd.DataFrame(df)

    fig = px.line(
        df,
        x="order_date",
        y="total_spend",
        color="customer_id",
        title="Customer Spend Over Time",
        labels={"total_spend": "Total Spend", "order_date": "Order Date"},
    )

    fig.update_layout(
        xaxis_title="Order Date", yaxis_title="Total Spend", legend_title="Customer ID"
    )

    return fig.to_html(full_html=False)
