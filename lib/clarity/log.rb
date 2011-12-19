module Clarity
  module Log
    def self.configure(opts)
      require 'log4r'
      require 'log4r/outputter/syslogoutputter'

      $log = Log4r::Logger.new "logger"
      if opts[:syslog]
        putter = Log4r::SyslogOutputter.new File.basename($0)
        putter.formatter = Log4r::PatternFormatter.new :pattern => "%l -- %m"
      else
        putter = Log4r::StderrOutputter.new File.basename($0)
        putter.formatter = Log4r::PatternFormatter.new :pattern => "[%d] %l -- %m"
      end
      putter.level = Log4r::DEBUG
      $log.outputters = putter
      $log.level = Log4r::DEBUG
    end
  end
end
