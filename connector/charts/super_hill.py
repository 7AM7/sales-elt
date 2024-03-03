import pandas as pd
import plotly.express as px


@render(render_type="html")  # type: ignore # noqa
def r(df, *args, **kwargs):
    df = pd.DataFrame(df)

    fig = px.line(
        df,
        x="order_date",
        y="cumulative_spend",
        color="customer_id",
        title="Cumulative Spend Over Time by Customer",
        labels={"cumulative_spend": "Cumulative Spend", "order_date": "Order Date"},
    )

    fig.update_layout(
        xaxis_title="Order Date", yaxis_title="Cumulative Spend", legend_title="Customer ID"
    )
    return fig.to_html(full_html=False)
