import pandas as pd
import plotly.express as px


@render(render_type="html")  # type: ignore # noqa
def r(df, *args, **kwargs):
    df = pd.DataFrame(df)

    fig = px.bar(
        df,
        x="city",
        y="total_products_sold",
        title="Total Products Sold in Each City",
        labels={"total_products_sold": "Total Products Sold", "city": "City"},
        color="total_products_sold",
        color_continuous_scale=px.colors.sequential.Viridis,
    )
    return fig.to_html(full_html=False)
