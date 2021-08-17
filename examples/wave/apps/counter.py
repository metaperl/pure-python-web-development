from h2o_wave import Q, main, app, ui


@app('/counter')
async def serve(q: Q):
    bean_count = q.client.bean_count or 0
    if q.args.increment:
        q.client.bean_count = bean_count = bean_count + 1

    q.page['beans'] = ui.form_card(
        box='1 1 1 2',
        items=[
            ui.button(
                name='increment',
                label='Click me!',
                caption=f'{bean_count} beans',
                primary=True,
            ),
        ],
    )
    await q.page.save()