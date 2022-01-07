# personal reminder: learn and use some sort of design pattern in next project.


from pathlib import Path

# Explicit imports to satisfy Flake8
# My own imports, starting at  filedialog
from tkinter import (
    Tk,
    Canvas,
    Entry,
    Text,
    Button,
    PhotoImage,
    filedialog,
    INSERT,
    Menu,
    ttk,
    StringVar,
    Spinbox,
)

# YT-DLP to download video on click
# chdir to change operational directory before download to specified path in entry field 2, path to specify log path
from yt_dlp import YoutubeDL
from os import chdir, path, startfile

# import date and time tools
from datetime import datetime

dt = datetime.now()


# <editor-fold desc="Asset Acquisition">


# access external assets
default = "./assets"
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(default)


# defines location of assets for access
def relative_to_assets(path_core: str) -> Path:
    return ASSETS_PATH / Path(path_core)


# </editor-fold>


# <editor-fold desc="Core Window">

# defines window
window = Tk()

window.geometry("1280x720")
window.configure(bg="#FFFFFF")
window.title("limetube")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=720,
    width=1280,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)
# </editor-fold>

# <editor-fold desc="Background color blocks (purple)">

# large purple background
canvas.place(x=0, y=0)
main_bg_img = PhotoImage(file=relative_to_assets("image_1.png"))
main_bg = canvas.create_image(636.0, 361.0, image=main_bg_img)

# url purple background
url_bg_img = PhotoImage(file=relative_to_assets("image_2.png"))
url_bg = canvas.create_image(638.0, 361.0, image=url_bg_img)
# </editor-fold>

# <editor-fold desc="Interface Title">

# title image (yt-dlp interface title)
title_img = PhotoImage(file=relative_to_assets("image_4.png"))
title = canvas.create_image(259.0, 88.0, image=title_img)
# </editor-fold>

# <editor-fold desc="URL Entry">

# URL entry text box
entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(636.5, 360.5, image=entry_image_1)
url_entry = Entry(font=("Freehand", 15), bg="#FFFFFF", highlightthickness=0)
url_entry.place(x=263.0, y=335.0, width=747.0, height=46.0)

# URL prompt text
canvas.create_text(
    254.0, 296.0, anchor="nw", text="URL:", fill="#000000", font=("Freehand", 30 * -1)
)


# </editor-fold>


# Sets directory, DLs vid, and runs logger functions
def click():
    bar_ret()
    # first section downloads file into specified directory
    save_loc = filedialog.askdirectory()
    bar_start()
    url = url_entry.get()
    print(url_entry.get())
    ydl_opts = {}
    chdir(save_loc)
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(["ytsearch:" + url])
    # runs logger after video is specified
    run_log()


# <editor-fold desc="DL Video Button GUI">

# select DL location and start DL button
dl_vid_img = PhotoImage(file=relative_to_assets("button_1.png"))
dl_button = Button(
    image=dl_vid_img,
    borderwidth=0,
    highlightthickness=0,
    command=click,
    relief="raised",
)
dl_button.place(x=908.0, y=565.0, width=328.0, height=120.0)


# </editor-fold>


# Sets directory, DLs audio, and runs logger functions
def audio():
    bar_ret()
    # first section downloads audio file into specified directory
    save_loc = filedialog.askdirectory()
    bar_start()
    url = url_entry.get()
    print(url_entry.get())
    ydl_opts = {
        "format": "ba",
        "postprocessor": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "wav",
                "preferredquality": "192",
            }
        ],
    }
    chdir(save_loc)
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(["ytsearch:" + url])
    # runs logger after video is specified
    run_log()


# <editor-fold desc="DL Audio Only Button GUI">

# DL audio only button
dl_audio_img = PhotoImage(file=relative_to_assets("button_4.png"))
dl_audio = Button(
    image=dl_audio_img,
    borderwidth=0,
    highlightthickness=0,
    command=audio,
    relief="raised",
)
dl_audio.place(x=917.0, y=500.0, width=309.0, height=52.0)
# </editor-fold>


# View Full Log Functions
def view_log():
    f_name = "limelog.txt"
    directory = path.join(path.expanduser('~'), 'Documents', f_name)
    startfile(str(directory))


# <editor-fold desc="View Full Log Button GUI">

# full log view button
view_log_img = PhotoImage(file=relative_to_assets("button_5.png"))
log_button = Button(
    image=view_log_img,
    borderwidth=0,
    highlightthickness=0,
    command=view_log,
    relief="raised",
)
log_button.place(x=935.0, y=242.0, width=213.0, height=20.0)
# </editor-fold>

# <editor-fold desc="Logger output GUI">

# Logger output box background
log_bg_img = PhotoImage(file=relative_to_assets("image_5.png"))
log_bg = canvas.create_image(882.0, 153.0, image=log_bg_img)

# Logger text box
text1 = Text(width=30, height=30)
text1.place(x=580.0, y=60.0, width=600.0, height=160.0)


# </editor-fold>

# Define video logger
def run_log():
    # first block grabs title of video
    url = url_entry.get()
    print(url_entry.get())
    ydl_opts = {}
    with YoutubeDL(ydl_opts) as ydl:
        data = ydl.extract_info(url, download=False)
    # second block which write the log.txt and the live DL history output.
    # TODO add a def and call for chg_log where if called, it sets different log_path and sets as default location
    f_name = "limelog.txt"
    with open(path.join(path.expanduser('~'), 'Documents', f_name), "a+") as hdl:
        log_line = str(url_entry.get())
        hdl.write("\n")
        hdl.write(data["title"])
        hdl.write("  ")
        hdl.write(str(dt))
        hdl.write("  ")
        hdl.write(log_line)
        hdl.close()
        text1.insert(INSERT, (data["title"]) + "  " + str(dt))
        text1.insert(INSERT, "\n")


# <editor-fold desc="Progress Bar GUI">

# Progress bar background
pb_bg_img = PhotoImage(file=relative_to_assets("image_3.png"))
pb_bg = canvas.create_image(640.0, 624.0, image=pb_bg_img)

# Progress Bar widget
pb = ttk.Progressbar(window, orient="horizontal", length=500, mode="determinate")
pb.place(x=440, y=600, width=400, height=40)


# </editor-fold>

# Progress bar update function
def bar_start():
    pb["value"] = 20
    window.update_idletasks()
    pb.step(1)

    pb["value"] = 40
    window.update_idletasks()
    pb.step(1)

    pb["value"] = 50
    window.update_idletasks()
    pb.step(1)
    pb["value"] = 100


# returns progress bar to zero when starting a new download
def bar_ret():
    pb["value"] = 0


def lt_dark():
    global canvas, main_bg_img, main_bg, url_bg_img, url_bg, pb_bg_img, pb_bg, title_img, title
    global log_bg_img, log_bg, dl_vid_img, dl_button, button_image_2, button_2, button_image_3, button_3
    global dl_audio_img, dl_audio, log_button, view_log_img, entry_image_1, entry_bg_1
    canvas.config(bg="#73689F")
    main_bg_img = PhotoImage(file=relative_to_assets("image_11.png"))
    main_bg = canvas.create_image(636.0, 361.0, image=main_bg_img)
    url_bg_img = PhotoImage(file=relative_to_assets("image_22.png"))
    url_bg = canvas.create_image(638.0, 361.0, image=url_bg_img)
    canvas.create_text(
        254.0,
        296.0,
        anchor="nw",
        text="URL:",
        fill="#FFFFFF",
        font=("Freehand", 30 * -1),
    )
    title_img = PhotoImage(file=relative_to_assets("image_44.png"))
    title = canvas.create_image(259.0, 88.0, image=title_img)
    dl_vid_img = PhotoImage(file=relative_to_assets("button_11.png"))
    dl_button = Button(
        image=dl_vid_img,
        borderwidth=0,
        highlightthickness=0,
        command=click,
        relief="raised",
    )
    dl_button.place(x=908.0, y=565.0, width=328.0, height=120.0)
    dl_audio_img = PhotoImage(file=relative_to_assets("button_44.png"))
    dl_audio = Button(
        image=dl_audio_img,
        borderwidth=0,
        highlightthickness=0,
        command=audio,
        relief="raised",
    )
    dl_audio.place(x=917.0, y=500.0, width=309.0, height=52.0)
    view_log_img = PhotoImage(file=relative_to_assets("button_55.png"))
    log_button = Button(
        image=view_log_img,
        borderwidth=0,
        highlightthickness=0,
        command=view_log,
        relief="raised",
    )
    log_button.place(x=935.0, y=242.0, width=213.0, height=20.0)
    log_bg_img = PhotoImage(file=relative_to_assets("image_55.png"))
    log_bg = canvas.create_image(882.0, 153.0, image=log_bg_img)
    pb_bg_img = PhotoImage(file=relative_to_assets("image_33.png"))
    pb_bg = canvas.create_image(640.0, 624.0, image=pb_bg_img)
    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(636.5, 360.5, image=entry_image_1)


def lt_light():
    global canvas, main_bg_img, main_bg, url_bg_img, url_bg, pb_bg_img, pb_bg, title_img, title
    global log_bg_img, log_bg, dl_vid_img, dl_button, button_image_2, button_2, button_image_3, button_3
    global dl_audio_img, dl_audio, log_button, view_log_img, entry_image_1, entry_bg_1
    canvas.config(bg="white")
    main_bg_img = PhotoImage(file=relative_to_assets("image_1.png"))
    main_bg = canvas.create_image(636.0, 361.0, image=main_bg_img)
    url_bg_img = PhotoImage(file=relative_to_assets("image_2.png"))
    url_bg = canvas.create_image(638.0, 361.0, image=url_bg_img)
    canvas.create_text(
        254.0,
        296.0,
        anchor="nw",
        text="URL:",
        fill="#000000",
        font=("Freehand", 30 * -1),
    )
    title_img = PhotoImage(file=relative_to_assets("image_4.png"))
    title = canvas.create_image(259.0, 88.0, image=title_img)
    dl_vid_img = PhotoImage(file=relative_to_assets("button_1.png"))
    dl_button = Button(
        image=dl_vid_img,
        borderwidth=0,
        highlightthickness=0,
        command=click,
        relief="raised",
    )
    dl_button.place(x=908.0, y=565.0, width=328.0, height=120.0)
    dl_audio_img = PhotoImage(file=relative_to_assets("button_4.png"))
    dl_audio = Button(
        image=dl_audio_img,
        borderwidth=0,
        highlightthickness=0,
        command=audio,
        relief="raised",
    )
    dl_audio.place(x=917.0, y=500.0, width=309.0, height=52.0)
    view_log_img = PhotoImage(file=relative_to_assets("button_5.png"))
    log_button = Button(
        image=view_log_img,
        borderwidth=0,
        highlightthickness=0,
        command=view_log,
        relief="raised",
    )
    log_button.place(x=935.0, y=242.0, width=213.0, height=20.0)
    log_bg_img = PhotoImage(file=relative_to_assets("image_5.png"))
    log_bg = canvas.create_image(882.0, 153.0, image=log_bg_img)
    pb_bg_img = PhotoImage(file=relative_to_assets("image_3.png"))
    pb_bg = canvas.create_image(640.0, 624.0, image=pb_bg_img)
    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(636.5, 360.5, image=entry_image_1)


def light_mode():
    global canvas, main_bg_img, main_bg, url_bg_img, url_bg, pb_bg_img, pb_bg, title_img, title
    global log_bg_img, log_bg, dl_vid_img, dl_button, button_image_2, button_2, button_image_3, button_3
    global dl_audio_img, dl_audio, log_button, view_log_img, entry_image_1, entry_bg_1
    canvas.config(bg="white")
    main_bg_img = PhotoImage(file=relative_to_assets("image_1lt.png"))
    main_bg = canvas.create_image(636.0, 361.0, image=main_bg_img)
    url_bg_img = PhotoImage(file=relative_to_assets("image_2lt.png"))
    url_bg = canvas.create_image(638.0, 361.0, image=url_bg_img)
    canvas.create_text(
        254.0, 296.0, anchor="nw", text="URL:", fill="black", font=("Freehand", 30 * -1)
    )
    title_img = PhotoImage(file=relative_to_assets("image_4lt.png"))
    title = canvas.create_image(259.0, 88.0, image=title_img)
    dl_vid_img = PhotoImage(file=relative_to_assets("button_1lt.png"))
    dl_button = Button(
        image=dl_vid_img,
        borderwidth=0,
        highlightthickness=0,
        command=click,
        relief="raised",
    )
    dl_button.place(x=908.0, y=565.0, width=328.0, height=120.0)
    dl_audio_img = PhotoImage(file=relative_to_assets("button_2lt.png"))
    dl_audio = Button(
        image=dl_audio_img,
        borderwidth=0,
        highlightthickness=0,
        command=audio,
        relief="raised",
    )
    dl_audio.place(x=917.0, y=500.0, width=309.0, height=52.0)
    view_log_img = PhotoImage(file=relative_to_assets("button_3lt.png"))
    log_button = Button(
        image=view_log_img,
        borderwidth=0,
        highlightthickness=0,
        command=view_log,
        relief="raised",
    )
    log_button.place(x=935.0, y=242.0, width=213.0, height=20.0)
    log_bg_img = PhotoImage(file=relative_to_assets("image_5lt.png"))
    log_bg = canvas.create_image(882.0, 153.0, image=log_bg_img)
    pb_bg_img = PhotoImage(file=relative_to_assets("image_3lt.png"))
    pb_bg = canvas.create_image(640.0, 624.0, image=pb_bg_img)
    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))


def dark_mode():
    global canvas, main_bg_img, main_bg, url_bg_img, url_bg, pb_bg_img, pb_bg, title_img, title
    global log_bg_img, log_bg, dl_vid_img, dl_button, button_image_2, button_2, button_image_3, button_3
    global dl_audio_img, dl_audio, log_button, view_log_img, entry_image_1, entry_bg_1
    canvas.config(bg="black")
    main_bg_img = PhotoImage(file=relative_to_assets("image_1dk.png"))
    main_bg = canvas.create_image(636.0, 361.0, image=main_bg_img)
    url_bg_img = PhotoImage(file=relative_to_assets("image_2dk.png"))
    url_bg = canvas.create_image(638.0, 361.0, image=url_bg_img)
    canvas.create_text(
        254.0, 296.0, anchor="nw", text="URL:", fill="white", font=("Freehand", 30 * -1)
    )
    title_img = PhotoImage(file=relative_to_assets("image_4dk.png"))
    title = canvas.create_image(259.0, 88.0, image=title_img)
    dl_vid_img = PhotoImage(file=relative_to_assets("button_1dk.png"))
    dl_button = Button(
        image=dl_vid_img,
        borderwidth=0,
        highlightthickness=0,
        command=click,
        relief="raised",
    )
    dl_button.place(x=908.0, y=565.0, width=328.0, height=120.0)
    dl_audio_img = PhotoImage(file=relative_to_assets("button_2dk.png"))
    dl_audio = Button(
        image=dl_audio_img,
        borderwidth=0,
        highlightthickness=0,
        command=audio,
        relief="raised",
    )
    dl_audio.place(x=917.0, y=500.0, width=309.0, height=52.0)
    view_log_img = PhotoImage(file=relative_to_assets("button_3dk.png"))
    log_button = Button(
        image=view_log_img,
        borderwidth=0,
        highlightthickness=0,
        command=view_log,
        relief="raised",
    )
    log_button.place(x=935.0, y=242.0, width=213.0, height=20.0)
    log_bg_img = PhotoImage(file=relative_to_assets("image_5dk.png"))
    log_bg = canvas.create_image(882.0, 153.0, image=log_bg_img)
    pb_bg_img = PhotoImage(file=relative_to_assets("image_3dk.png"))
    pb_bg = canvas.create_image(640.0, 624.0, image=pb_bg_img)
    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))


# menu bar
def menu_bar():
    m_bar = Menu(window)
    # UI color change menu      # TODO UI color change menu
    m_color = Menu(m_bar, tearoff=0)
    m_color.add_command(label="limetube light", command=lt_light)
    m_color.add_command(label="limetube dark", command=lt_dark)
    m_color.add_command(label="Day Mode", command=light_mode)
    m_color.add_command(label="Night Mode", command=dark_mode)
    m_bar.add_cascade(label="Change Color Scheme", menu=m_color)
    window.config(menu=m_bar)


menu_bar()

# prevents window resize, and closes window when exit out.
window.resizable(False, False)
window.mainloop()
