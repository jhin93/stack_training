const jwt = require('jsonwebtoken');

const authenticateToken = (req, res, next) => {
    // Get the token from the header
    const authHeader = req.headers['authorization'];
    const token = authHeader && authHeader.split(' ')[1]; // Bearer <token>
    if (!token) {
        return res.status(401).json({ message: 'Access token is required' });
    }

    // Verify the token
    jwt.verify(token, process.env.JWT_SECRET, (err, decoded) => {
        if (err) {
            console.log("Token verification error: ", err);
            return res.status(403).json({ message: 'Invalid or expired token' });
        }
        
        // If token is valid, attach the decoded user information to the request object
        req.user = {
            userId: decoded.userId,
            email: decoded.email,
        }
        next(); // Proceed to the next middleware or route handler
    });
};

module.exports = authenticateToken;