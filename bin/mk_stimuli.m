srate = 44100;  % samp/s
tone_dur = 20;  % in ms
ramp_dur = 5;

peak_vol = 0.00;    % out of 1 for full dynamic range of wav file
freq = [200, 300, 400, 500];

write_html = true;

% first construct timebase
t = [0:(1/srate):(tone_dur/1000)]';  % in s

% then construct ramp
window = peak_vol * ones(size(t));
win_len = floor(ramp_dur*srate/1000);
window(1:win_len) = linspace(0, peak_vol, win_len);
window(end-win_len+1:end) = linspace(peak_vol, 0, win_len);

% generate sounds and save
for i = 1:length(freq)
    snd = sin(t*freq(i)*2*pi);
    snd = snd.*window;
    
    if freq(i) < 1000
        fname = sprintf('sound_%03.fHz.wav', freq(i));
    else
        fname = sprintf('sound_%04.fHz.wav', freq(i));
    end;
    
    audiowrite(fname, [snd, snd], srate, 'BitsPerSample', 16); 
    
end;

% make html sample

fid = fopen('test.html', 'w');
fprintf(fid, '<!DOCTYPE html><html><head></head><body>\n');

for i = 1:length(freq)
    
    if freq(i) < 1000
        fname = sprintf('sound_%03.fHz.wav', freq(i));
    else
        fname = sprintf('sound_%04.fHz.wav', freq(i));
    end;
    
    fprintf(fid, '<h3>%s</h3>\n<audio controls>\n', fname); 
    fprintf(fid, '\t<source src="%s" type="audio/wav">\n', fname);
    fprintf(fid, '</audio></br>\n');
end;

fprintf(fid, '</body></html>\n');
fclose(fid);

