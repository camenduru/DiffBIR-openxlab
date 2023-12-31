import os
os.chdir(f"/home/xlab-app-center")
os.system(f"git clone -b openxlab https://github.com/camenduru/DiffBIR /home/xlab-app-center/DiffBIR")
os.chdir(f"/home/xlab-app-center/DiffBIR")
os.system(f"git lfs install")
os.system(f"git pull")
os.system(f"git reset --hard")

# os.system(f"wget https://huggingface.co/lxq007/DiffBIR/resolve/main/face_full_v1.ckpt -O /home/xlab-app-center/face_full_v1.ckpt")
# os.system(f"wget https://huggingface.co/lxq007/DiffBIR/resolve/main/face_swinir_v1.ckpt -O /home/xlab-app-center/face_swinir_v1.ckpt")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/camenduru/DiffBIR/resolve/main/face_full_v1.ckpt -d /home/xlab-app-center/models -o face_full_v1.ckpt")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/camenduru/DiffBIR/resolve/main/face_swinir_v1.ckpt -d /home/xlab-app-center/models -o face_swinir_v1.ckpt")
os.system(f"python gradio_diffbir.py --ckpt /home/xlab-app-center/face_full_v1.ckpt --config /home/xlab-app-center/DiffBIR/configs/model/cldm.yaml --reload_swinir --swinir_ckpt /home/xlab-app-center/face_swinir_v1.ckpt")

# os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/camenduru/DiffBIR/resolve/main/general_full_v1.ckpt -d /home/xlab-app-center/models -o general_full_v1.ckpt")
# os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/camenduru/DiffBIR/resolve/main/general_swinir_v1.ckpt -d /home/xlab-app-center/models -o general_swinir_v1.ckpt")
# os.system(f"wget https://huggingface.co/camenduru/DiffBIR/resolve/main/general_full_v1.ckpt -O /home/xlab-app-center/general_full_v1.ckpt")
# os.system(f"wget https://huggingface.co/camenduru/DiffBIR/resolve/main/general_swinir_v1.ckpt -O /home/xlab-app-center/general_swinir_v1.ckpt")
# os.system(f"python gradio_diffbir.py --ckpt /home/xlab-app-center/general_full_v1.ckpt --config /home/xlab-app-center/DiffBIR/configs/model/cldm.yaml --reload_swinir --swinir_ckpt /home/xlab-app-center/general_swinir_v1.ckpt")