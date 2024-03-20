
import streamlit as st

print("page reloaded")
st.set_page_config(
    page_title="축구선수 스쿼드11",
    page_icon="./ball.png"
)
st.title("hello streamlit")
st.text("자신만의 축구선수 스쿼드를 만들어보세여")

type_emoji_dict = {
    "공격수fw": "⚽",
    "미드필더mf":"🦭",
    "수비수df":"🐲",
    "골키퍼gk":"⚽"
}



initial_pokemons = [
    {
        "name": "손흥민",
        "types": ["공격수fw"],
        "image_url": "https://i.namu.wiki/i/5XCuCI0ND55dhXQx4aN3pno4PJj_MaL2d_TbV2j9SyBCunO52j0cIfoEv4-XdkHl21MOR1S2AKByytbxH0KHEQKdtpsL7vvXw8catt8iXi-9RsDaDZ3kUzqOSju-Qr-bfaJsWAO-1tpRto0GgrSAJA.webp"
    },
    {
        "name": "박지성",
        "types": ["미드필더mf"],
        "image_url": "https://i.namu.wiki/i/EfB5cnKh8JI_1HGFTFZwacvDfYKO-iSJsWC7DbnC36d05RauAKh3jQVmpnzu8v7scFXqg6z3lbOGRs9JuoUS9GheQ8yHhVGn24u4dhciau0AZW9r_3p1ZrrbQ9oCjtjGedF2N77gq_hLNuCW53G3Eg.webp",
    },
    {
        "name": "이강인",
        "types": ["미드필더mf"],
        "image_url": "https://i.namu.wiki/i/XHBvlA4wiVMJteIkdVq_7R7SbRvSHbGhbOywqoTK3RdccDKtu5Mq8Ik75cBfIbxXIOkmrYzjXQOzjvuFYeCA7Nx0-a0twhEBWmH57KRYGnGngadPy_V7dsw6xXekpsjoHRc2uMheMeAfVsXp-pkNqw.webp",
    },
    {
        "name": "김민재",
        "types": ["수비수df"],
        "image_url": "https://i.namu.wiki/i/-LzGBVg5nh4ogh5Hyy-FScRmFkTwIJI3JMxPnqQLMgd4r0phxQpPsKM5mXUSeziKUVhtzy-SdrAwKZmTYmhkVXrWPsND-6OP6APcxOosa0xf4WIrFSzgeDqi1dLmnD3QfiKw1utdjL-IkHIbM_9UQg.webp"
    },
    {
        "name": "김영권",
        "types": ["수비수df"],
        "image_url": "https://i.namu.wiki/i/Pe-25a-urukGWBLIFhBblMVRdFzFLdeeunmoIizRDXop1ofCoo_7kflsE4LIyJhkDy7a2wI3JkFCqAA0EzI_a2ci_uBgnTYgQXg1LYPM6wVjhEKrNGKpWOPHU0MhZoPprfbsXeoGXKBF3D8l1rDcjQ.webp"
    },
    {
        "name": "조현우",
        "types": ["골키퍼gk"],
        "image_url": "https://i.namu.wiki/i/Vx3aWASFPMvJuLt5iIAeGh-aqYctqaliAwgpoNz41m5tmtw9t8PXWTNeVMZY5LlVIVJ4PM8jDYZirGVq_rqIkrse5fp4Ohjk8ZzqZnI_xhpcr_w1cgge-OzP5KA_zQi0bxGb14WJudkhqEskgAJ33A.webp"
    },
]

example_pokemon = {
    "name": "차범근",
    "types": ["공격수fw"],
    "image_url": "https://i.namu.wiki/i/o8CcT2DqUynTokQ41I7gU7z-nJzrNYpVlC-FjyHRrdyRzF0JZttBB99xrNkBSdXNLZyBQcnP02Hn3_H2vQmza7TpCGcmbLYD-sk6F5F3ySyaNfCJ6GyKZ1APehtCphbvsndIcZuCwSngRmG91av6cw.webp"
}


if "pokemons" not in st.session_state:
    st.session_state.pokemons = initial_pokemons

auto_complete = st.toggle("예시 데이터로 채우기")
print("page reload, auto_complete", auto_complete)
with st.form(key='form'):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input(label="선수이름", value=example_pokemon["name"] if auto_complete else"")
    with col2:
        types = st.multiselect(label="포지션",options=list(type_emoji_dict.keys()),max_selections=2,
        default=example_pokemon["types"] if auto_complete else [])
    image_url = st.text_input(label="선수사진",
    value = example_pokemon["image_url"] if auto_complete else "")
    submit = st.form_submit_button(label="Submit")
    if submit:
        if not name:
            st.error("선수의 이름을 입력해주세요")
        elif len(types) == 0:
            st.error("적어도 한개 선택해주세요")
        else:
            st.success("선수를 추가할 수 있습니다.")
            st.session_state.pokemons.append({
                "name": name,
                "types": types,
                "image_url": image_url if image_url else "./default.png"
})



for i in range(0, len(st.session_state.pokemons), 3):
    row_pokemons = st.session_state.pokemons[i:i+3]
    cols = st.columns(3)
    for j in range(len(row_pokemons)):
        with cols[j]:
            pokemon = row_pokemons[j]
            with st.expander(label=f"**{i+j+1}. {pokemon["name"]}**", expanded = True):
                st.subheader(pokemon["name"])
                st.image(pokemon["image_url"])
                emoji_types = [f"{type_emoji_dict[x]} {x}" for x in pokemon["types"]]
                st.subheader(" / ".join(emoji_types))
                delete_button = st.button(label="삭제", key=i+j, use_container_width=True)
                if delete_button:
                    print("delete button clicked!")
                    del st.session_state.pokemons[i+j]
                    st.rerun()

                