const express = require('express');
const multer = require('multer');
const path = require('path');
const fs = require('fs');

const app = express();
const PORT = process.env.PORT || 4000;

const uploadDir = path.join(__dirname, 'uploads');
// Ensure uploads directory exists
if (!fs.existsSync(uploadDir)) {
  fs.mkdirSync(uploadDir, { recursive: true });
}

const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, uploadDir);
  },
  filename: function (req, file, cb) {
    cb(null, Date.now() + '-' + file.originalname);
  }
});
const upload = multer({ storage });

app.post('/upload', upload.single('file'), async (req, res) => {
  if (!req.file) {
    return res.status(400).json({ error: 'No file uploaded' });
  }

  const fileUrl = `/uploads/${req.file.filename}`;
  const response = { url: fileUrl };

  try {
    const fileData = await fs.promises.readFile(req.file.path);
    response.base64 = `data:${req.file.mimetype};base64,` + fileData.toString('base64');
  } catch (err) {
    // If reading fails, continue without base64 field
  }

  res.json(response);
});

app.use('/uploads', express.static(uploadDir));

app.listen(PORT, () => {
  console.log(`File uploader listening on port ${PORT}`);
});
