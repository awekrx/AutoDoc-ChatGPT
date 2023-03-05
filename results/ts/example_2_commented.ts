import * as http from "http";


/**
 * 
 * This type represents the HTTP methods that can be used for making requests.
 * @typedef {'GET' | 'POST' | 'PUT' | 'DELETE' | 'PATСH'} protocols
 */
type protocols = 'GET' | 'POST' | 'PUT' | 'DELETE' | 'PATСH'



/**
 * This class represents a server and creates an instance of http.Server. 
 * @class
 * 
 */
export default class Server {
    /**
     * A private property that holds an instance of http.Server.
     * @type {http.Server}
     * 
     */
    private server: http.Server;
    /**
     * A private property that holds the port number.
     * @type {string|number}
     * 
     */
    private port!: string | number;
    /**
     * Creates a new Server instance with the given serverResponse and serverError functions.
     * @constructor
     * @param {function} serverResponse - The function that will handle server response.
     * @param {function} serverError - The function that will handle server error.
     * 
     */
    constructor(serverResponse: (data: string, req: http.IncomingMessage, res: http.ServerResponse) => void, serverError: (req: http.IncomingMessage, res: http.ServerResponse) => void) {
        this.server = http
            .createServer((req: http.IncomingMessage, res: http.ServerResponse) => {
                if (req.method == "GET") {
                    if (req.url) {
                        let body = '';
                        req.on('data', chunk => {
                            body += chunk.toString();
                        });
                        req.on('end', () => {
                            res.setHeader('Content-Type', 'application/json');
                            try {
                                serverResponse(body, req, res);
                            } catch (error) {
                                serverError(req, res)
                            }
                        });
                    }
                }
            })
    }

    /**
     * 
     * Starts the server on the specified port.
     * @param {string|number} port - The port number on which the server will listen.
     * @returns {void}
     */
    public listen(port: string | number,) {
        this.port = port;
        this.server.listen(this.port);
    }
}
