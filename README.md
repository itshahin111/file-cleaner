File Cleaner Tool — Usage Instructions
🔹 Windows (EXE file ব্যবহার)

GitHub থেকে file_cleaner.exe ডাউনলোড করো।

ডাবল-ক্লিক করলেই টুল ওপেন হবে।

যে ফোল্ডার ক্লিন করতে চাও সেটা সিলেক্ট করো।

যেসব ফাইল ফরম্যাট ডিলিট করতে চাও (যেমন .jpg, .mp4, .pdf) সেগুলো চেকবক্স থেকে বেছে নাও।

Delete বাটনে ক্লিক করো — এক ক্লিকেই সব ডিলিট হয়ে যাবে। ✅
(Windows-এ Python ইনস্টল না থাকলেও .exe ফাইল কাজ করবে)





Linux / Ubuntu / Debian (Python File ব্যবহার)

Python3 আগে থেকেই থাকে (না থাকলে ইনস্টল করো):

sudo apt update
sudo apt install python3 python3-pip -y


প্রজেক্ট ডাউনলোড করো:

git clone https://github.com/itshahin111/file-cleaner.git
cd file-cleaner


(যদি requirements.txt থাকে তাহলে):

pip3 install -r requirements.txt


রান করো:

python3 src/file_cleaner.py


GUI ওপেন হবে → ফোল্ডার সিলেক্ট করো → ফাইল ফরম্যাট সিলেক্ট করো → Delete চাপো।

🔹 Important Notes

Backup রাখো – ডিলিট হয়ে গেলে রিস্টোর করা যাবে না।

Admin Permission লাগতে পারে যদি System Folder ক্লিন করো।

Linux এ চাইলে .desktop shortcut বানিয়ে নিতে পারো, Windows এ চাইলে .exe কে Start Menu তে যোগ করতে পারো।