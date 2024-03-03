import pandas as pd
import plotly.graph_objects as go


@render(render_type="html")  # type: ignore # noqa
def r(df, *args, **kwargs):
    df = pd.DataFrame(df)
    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=df["weather_conditions"],
            y=df["total_sales"],
            name="Total Sales",
            marker_color="indianred",
        )
    )

    fig.add_trace(
        go.Bar(
            x=df["weather_conditions"],
            y=df["average_sales_amount"],
            name="Average Sales Amount",
            marker_color="lightsalmon",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df["weather_conditions"],
            y=df["number_of_transactions"],
            name="  Number of Transactions",
            mode="lines+markers",
            yaxis="y2",
        )
    )

    fig.update_layout(
        title="Sales Metrics by Weather Conditions",
        xaxis_title="Weather Conditions",
        yaxis=dict(
            title="Sales Amount",
            titlefont=dict(color="indianred"),
            tickfont=dict(color="indianred"),
        ),
        yaxis2=dict(
            title="Num of Transactions",
            titlefont=dict(color="blue"),
            tickfont=dict(color="blue"),
            overlaying="y",
            side="right",
        ),
        barmode="group",
    )

    return fig.to_html(full_html=False)
