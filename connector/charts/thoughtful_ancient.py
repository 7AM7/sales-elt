import pandas as pd
import plotly.graph_objects as go


@render(render_type="html")  # type: ignore # noqa
def r(df, *args, **kwargs):
    df = pd.DataFrame(df)

    fig = go.Figure()
    for id, group in df.groupby("customer_id"):
        fig.add_trace(
            go.Scatter(
                x=group["week_start_date"],
                y=group["total_sales_amount"],
                mode="lines+markers",
                name=id,
            )
        )

    fig.update_layout(
        title="Weekly Sales Amount per Customer",
        xaxis_title="Week Starting Date",
        yaxis_title="Total Sales Amount",
        xaxis=dict(tickmode="auto", tickformat="%b %d", tickangle=45),
        legend_title_text="Customer ID",
        hovermode="x unified",
    )

    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor="LightPink")

    return fig.to_html(full_html=False)
